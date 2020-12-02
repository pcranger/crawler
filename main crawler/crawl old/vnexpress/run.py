import download

a = input("which paper would you like to download?")
if a.lower() == 'tuoitre':
    baseurl = "https://tuoitre.vn"
    url1 = "https://tuoitre.vn/suc-khoe/dinh-duong/trang-1.htm"
elif a.lower() == 'dantri':
    url1 = "https:// dantri.com.vn/suc-khoe/trang-1.htm"
elif a.lower() == 'vnexpress':
    url1 = "https://vnexpress.net/suc-khoe/dinh-duong-p2"
    pass
download.exec()
