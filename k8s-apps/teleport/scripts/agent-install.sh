curl -O https://get.gravitational.com/teleport-v9.2.4-linux-amd64-bin.tar.gz
tar -xzf teleport-v9.2.4-linux-amd64-bin.tar.gz
rm teleport-v9.2.4-linux-amd64-bin.tar.gz
cd teleport && sudo ./install
rm -rf teleport