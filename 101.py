import os
import dropbox
import dropbox.files import WriteMode

class TransferData:
    def __init__(self,accessToken):
        self.accessToken = accessToken

    def upload_file(self, fileFrom, fileTo):
        dbx= dropbox.Dropbox(self.accessToken)

        for root, dirs, files in os.walk(fileFrom):
            for fileName in files:
                local_path=os.path.join(root, filename)
                relative_path=os.path.relativepath(local_path, fileFrom)
                dropbox_path = os.path.join(fileTo, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path, mode=WriteMode('overwrite'))

def main():
    accessToken = 'sl.A0tjz0D61c3ogjyfhwTt6Lu6KUoLE40IaIjQoMDIWS72ueWr_M_7oy8TJr_31NqSD_Dl56plBehno6_tznIvcT3YEvnBQZguMTEeTLQS1fKGzVqD4qmODM5yu8A5BCbz0TeFxFo'
    transfer_data=transfer_data(accessToken)
    fileFrom= input("Enter the file path to tranfer: ")
    fileTo= input("Enter the full path to upload to drop box: ")
    transfer_data.upload_file(fileFrom,fileTo)
    print("Task completed, file moved.")


main()

    
