import os, time
import subprocess
from flask import Flask, request, jsonify, send_file
import logging as logger

from src.config import Config
from src.utils import Utils

logger.basicConfig(level=logger.INFO)


def create_app():

    app = Flask(__name__)

    @app.route("/process", methods=["POST"])
    def process_files():
        """
        process files with rebuild engine
        """

        Utils.truncate_folder(Config.input_path)
        Utils.truncate_folder(Config.output_path)

        file = request.files.get("file")
        if not file:
            return jsonify({"message": "please supply a file"})
        file.save(os.path.join(Config.input_path, file.filename))
        os.system(
            "glasswallCLI -config={0}/Config.ini -xmlconfig={0}/Config.xml".format(
                Config.config_path
            )
        )
        logger.info(os.system("ls -alh /usr/src/app/rebuild_files/output/Managed"))
        logger.info(os.system("cat /usr/src/app/rebuild_files/output/glasswallCLIProcess.log"))
        try:
            return send_file(
                Config.output_path + "/" + file.filename,
                attachment_filename=file.filename,
                as_attachment=True,
            )
        except Exception:
            return jsonify({"message":"failed"})

    return app
