# -*- coding: utf-8 -*-
#################################################################################
#
#   Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#   See LICENSE file for full copyright and licensing details.
#   License URL : <https://store.webkul.com/license.html/>
#
#################################################################################
import os
import logging

from odoo import http, _
from odoo.http import request
from odoo.exceptions import AccessError, UserError


_logger = logging.getLogger(__name__) 

class BackupController(http.Controller):
    
    
    @http.route('/backupfile/download', type='http', auth='user')
    def file_download(self, **kwargs):
        file_path = request.httprequest.args.get('path')   # The actual file path
        backup_location = request.httprequest.args.get('backup_location') or 'local'
        _logger.info(f"=====backup_location========= {backup_location} ====== file_path ====== {file_path}")
        try:
            # Read the file and return it as a response
            file_data = None
            with open(file_path, 'rb') as file:
                file_data = file.read()

            # Set the response headers for file download
            response = request.make_response(file_data)
            response.headers['Content-Disposition'] = f"attachment; filename={file_path.split('/')[-1]}" 
            response.mimetype = 'application/octet-stream'
            
            # Delete the remote backup file from Main Server
            if backup_location == 'remote':
                os.remove(file_path)

            return response
        except Exception as e:
            _logger.info(f"======= Backup File Download Error ======= {e} ========")
            raise UserError(e)
