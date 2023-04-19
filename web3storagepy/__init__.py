import os
import sys
import magic
import requests


class Web3Storage(object):
    def __init__(self):
        self.BASE_URL = "https://api.web3.storage/{}"

    # uploads and stores a file
    def upload(self, file: str, token: str):
        with open(file, "rb") as f:
            file_name = os.path.basename(file)
            # extension = os.path.splitext(file_name)[1]
            mime = magic.Magic(mime=True)
            content_type = mime.from_file(file)
            headers = {
                "Content-Type": content_type,
                "Authorization": f"Bearer {token}",
                "X-NAME": file_name
            }
            upload_endpoint = "upload"
            req = requests.post(self.BASE_URL.format(upload_endpoint), headers=headers, files={file_name: f})
            if req.status_code == 200:
                data = {
                    "STATUS_CODE": 200,
                    "RESPONSE": req.text
                }

                return data
            else:
                data = {
                    "RESPONSE": req.text
                }

                return data

    # retrieve information about an upload
    def status(self, cid: str, token: str):
        headers = {
            "Authorization": f"Bearer {token}"
        }
        status_endpoint = f"status/{cid}"
        req = requests.get(self.BASE_URL.format(status_endpoint), headers=headers)

        if req.status_code == 200:
            data = {
                "STATUS_CODE": 200,
                "RESPONSE": req.text
            }

            return data
        else:
            data = {
                "RESPONSE": req.text
            }

            return data

    # list previous uploads
    def user_uploads(self, token: str):
        headers = {
            "Authorization": f"Bearer {token}"
        }
        uploads_endpoint = "user/uploads"
        req = requests.get(self.BASE_URL.format(uploads_endpoint), headers=headers)

        return req.text

    # returns a single upload
    def get_upload(self, cid: str):
        # headers = {
        #     "Accept": "*/*",
        #     "Authorization": f"Bearer {token}"
        # }
        # endpoint = f"user/uploads/{cid}"
        # req = requests.get(self.BASE_URL.format(endpoint), headers=headers)
        #
        # return req.text
        link = f"https://{cid}.ipfs.w3s.link"
        return link

sys.modules[__name__] = Web3Storage()