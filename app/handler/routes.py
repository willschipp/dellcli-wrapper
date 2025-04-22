from flask import Blueprint, request, jsonify
import json
import subprocess
import tempfile
import os

main = Blueprint('main',__name__)

# tool location
absolute_path = os.path.abspath('tools/dellctl')

admin_token_command = "admin token --name TOKEN_NAME --jwt-signing-secret SECRET --access-token-expiration EXPIRATION --refresh-token-expiration REFRESH"

#admin token --name admin --jwt-signing-secret secret --access-token-expiration 30s --refresh-token-expiration 120m > Admin-Token

@main.route('/admin/token',methods=['POST'])
def get_token():
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

#dellctl --admin-token Admin-Token generate token --tenant csmtenant-test --access-token-expiration 100h --refresh-token-expiration 6000h --addr proxy-server.apps.ocp-control.powerflex.cto --insecure > tenant-perf.token.yml

tenant_token_command = '--admin-token ADMIN_TOKEN generate token --tenant TENANT_NAME --access-token-expiration TOKEN_EXPIRATION --refresh-token-expiration REFRESH_EXPIRATION --addr SERVER_ADDRESS --insecure'

@main.route('/tenant/token',methods=['POST'])
def get_tenant_token():
    # get and return the whole yaml
    # admin token
    admin_token = request.json.get("admin-token")
    # write it to a file
    temp_file = tempfile.NamedTemporaryFile(mode="w+",delete=False,suffix=".json")
    json.dump(admin_token,temp_file)
    temp_file.flush()
    # temp_file.write(admin_token)
    temp_file_path = temp_file.name   
    # tenant name
    tenant_name = request.json.get("tenant-name")
    # token expiration
    token_expiration = request.json.get("token-expiration")
    # refresh expiration
    refresh_expiration = request.json.get("refresh-expiration")
    # server
    server = request.json.get("server")
    # replace command
    command = tenant_token_command.replace("ADMIN_TOKEN",temp_file_path).replace("TENANT_NAME",tenant_name).replace("TOKEN_EXPIRATION",token_expiration).replace("REFRESH_EXPIRATION",refresh_expiration).replace("SERVER_ADDRESS",server)
    execute_command = absolute_path + " " + command
    print(execute_command)
    result = subprocess.run(execute_command,shell=True,capture_output=True,text=True)
    output = result.stdout if result.returncode == 0 else result.stderr

    if result.returncode != 0:
        # error
        return jsonify({
        'output':output,
        'returncode':result.returncode
        }),503
    #if no error
    return output,200    
