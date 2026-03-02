# activ
source ./myenv/bin/activate

rm -f data_scratch.deb
rm -f -r linux_datascratch

# The spec file determine the optiosn for the packaging with pyinstaller.
pyinstaller linux.spec -y

# Packaging this requries ruby. 
sudo apt install ruby

# Nessicary part of running the rub scripts. 
if which ruby >/dev/null && which gem >/dev/null; then
    export PATH="$(ruby -r rubygems -e 'puts Gem.user_dir')/bin:$PATH"
fi

# It also requires fpm, which helps with the deb package.
gem install fpm --user-install

mkdir -p linux_datascratch/opt
mkdir -p linux_datascratch/usr/share/applications
mkdir -p linux_datascratch/usr/share/icons/hicolor/scalable/apps
cp -r dist/main linux_datascratch/opt/datascratch
cp resources/Mini_Logo_Alantis_Learn_book.svg linux_datascratch/usr/share/icons/hicolor/scalable/apps/datascratch.svg
cp datascratch.desktop linux_datascratch/usr/share/applications

find linux_datascratch/opt/datascratch -type f -exec chmod 644 -- {} +
find linux_datascratch/opt/datascratch -type d -exec chmod 755 -- {} +
find linux_datascratch/usr/share -type f -exec chmod 644 -- {} +
chmod +x linux_datascratch/opt/datascratch/datascratch
rm most_recent_installers/data_scratch.deb
fpm -C linux_datascratch -s dir -t deb -n "datascratch" -v 0.1.0  \
  --description "DataScratch is software intended to teach novices the core concepts of data science, without the prerequisite of knowing how to program. DataScratch achieves this via an intuitive drag and drop interface modeled after scratch." \
  --maintainer "Charles Bennington <https://github.com/cbennington852/DataScratch/issues>" \
  -p most_recent_installers/data_scratch.deb