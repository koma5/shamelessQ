# run this file to generate docker.ini
. secret.txt
cat <<EOF > docker.ini
[httpd]
enable_cors = true

[cors]
origins = *
credentials = true

[admins]
admin = ${ADMINPASSWORD}

EOF
