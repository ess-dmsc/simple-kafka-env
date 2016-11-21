Vagrant.configure(2) do |config|
  config.ssh.shell = "bash -c 'BASH_ENV=/etc/profile exec bash'"

  config.vm.define "kafka-env" do |dm|
    dm.vm.box = "esss/centos-7.1-desktop"
    dm.vm.synced_folder "code", "/home/vagrant/code", owner: "vagrant", create: "true"
    dm.vm.hostname = "kafka-env"

    dm.vm.provider "virtualbox" do |vb|
      vb.name = "Kafka-Env"
      vb.gui = false
      vb.cpus = "1"
      vb.memory = "1024"
    end
  end

  config.vm.provision "shell", "keep_color": true, "path": "provisioning.sh"

end
