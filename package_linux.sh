# activ
source ./myenv/bin/activate

# The spec file determine the optiosn for the packaging with pyinstaller.
pyinstaller main.spec -y

# Packaging this requries ruby. 
#sudo apt install ruby

# It also requires fpm, which helps with the deb package.
#gem install fpm --user-install

