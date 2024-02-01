fileName = input("File Name: ").lower().strip()
startChar = '.'
extension = ''
startIndex = fileName.rfind(startChar)
extension = fileName[startIndex:]
match extension:
    case ".gif":
        print("image/gif")
    case ".jpg" | ".jpeg":
        print("image/jpeg")
    case ".png":
        print("image/png")
    case ".pdf":
        print("application/pdf")
    case ".txt":
        print("text/plain")
    case ".zip":
        print("application/zip")
    case _:
        print("application/octet-stream")
