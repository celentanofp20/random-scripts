from letterboxd_login import login_to_letterboxd
from letterboxd_get_image_src import get_image_src

password = "acz8ehd9fkh.FMW_heb"
username = "frankie.celentano@yahoo.com"

# Call the login function with the username and password
d = login_to_letterboxd(username, password)
get_image_src(d)
