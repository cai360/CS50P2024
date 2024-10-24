FileName = input("input a file name: ").replace(" ", "").lower()


if ".gif" in FileName:
    print("image/gif")
elif ".jpg" in FileName:
    print("image/jpeg")
elif ".jpeg" in FileName:
    print("image/jpeg")
elif ".png" in FileName:
    print("image/png")
elif ".pdf" in FileName:
    print("application/pdf")
elif ".txt" in FileName:
    print("text/plain")
elif ".zip" in FileName:
    print("application/zip")
else:
    print("application/octet-stream")
