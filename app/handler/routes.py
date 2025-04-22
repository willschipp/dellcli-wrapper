from flask import Blueprint, request, jsonify
from loguru import logger
import json
import subprocess
import os

main = Blueprint('main',__name__)

# tool location
absolute_path = os.path.abspath('tools/dellctl')

admin_token_command = "admin token --name TOKEN_NAME --jwt-signing-secret SECRET --access-token-expiration EXPIRATION --refresh-token-expiration REFRESH"

#admin token --name admin --jwt-signing-secret secret --access-token-expiration 30s --refresh-token-expiration 120m > Admin-Token

@main.route('/admin/token',methods=['POST'])
def get_token():
    logger.info(f"here we go...")
    # get the json
    # need the token name
    token_name = request.json.get('token-name')
    # need the secret
    signing_secret = request.json.get('jwt-signing-secret')
    # need the expiration
    token_expiration = request.json.get('access-token-expiration')
    # need the refresh
    refresh_expiration = request.json.get('refresh-token-expiration')
    # convert to commands
    command = admin_token_command.replace('TOKEN_NAME',token_name).replace('SECRET',signing_secret).replace('EXPIRATION',token_expiration).replace('REFRESH',refresh_expiration)
    execute_command = absolute_path + " " + command
    result = subprocess.run(execute_command,shell=True,capture_output=True,text=True)
    output = result.stdout if result.returncode == 0 else result.stderr

    return jsonify({
        'output':output,
        'returncode':result.returncode
    }),200

