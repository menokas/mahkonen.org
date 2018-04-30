# Cottage service
## Sonos API HTTP
* http://codenugget.co/2016/05/22/sunday-hacking-sonos-home-part1.html
* http://codenugget.co/2016/08/29/sunday-hacking-sonos-home-part2.html

```
cd sonos_docker
(docker build -t sonos-http-api .)
docker run -d --net=host sonos-http-api

curl http://localhost:5005/zones

## TBD! Kbernetes and Raspberry Pi (https://blog.hypriot.com/post/setup-kubernetes-raspberry-pi-cluster/)
```
wget https://github.com/hypriot/image-builder-rpi/releases/download/v1.8.0/hypriotos-rpi-v1.8.0.img.zip
```
Unpack and flash 

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" > /etc/apt/sources.list.d/kubernetes.list
apt-get update
apt-get upgrade
apt-get dist-upgrade
apt-get install -y kubeadm
...
reboot
...
kubeadm init --pod-network-cidr 10.244.0.0/16 --apiserver-advertise-address=<WiFi IP>

k8s.gcr.io/kube-apiserver-arm
k8s.gcr.io/kube-scheduler-arm
k8s.gcr.io/kube-controller-manager-arm
k8s.gcr.io/etcd-arm
k8s.gcr.io/pause-arm

sudo cp /etc/kubernetes/admin.conf $HOME/
sudo chown $(id -u):$(id -g) $HOME/admin.conf
export KUBECONFIG=$HOME/admin.conf
kubeadm join --token=bb14ca.e8bbbedf40c58788 192.168.0.34