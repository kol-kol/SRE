resource "terraform_data" "cloud_init_cicustom_file" {
    provisioner "local-exec" {
        command = "sshpass -p '($password)' scp ./cloud-init.yml root@($hostname or ip):/var/lib/vz/snippets/"
    }
}

resource "proxmox_vm_qemu" "TerraformVM" {
    depends_on = [terraform_data.cloud_init_cicustom_file]
    target_node = "pve1"
    name = "TerraformVM"
    desc = "ВМ созданная из Terraform"
    bios = "seabios"
    boot = "order=scsi0;net0"
    agent = 1
    clone = "altlinux-p10-cloud"
    full_clone = true
    memory = 2048
    balloon = 1024
    sockets = 1
    cores = 1
    vcpus = 1
    cpu = "kvm64"
    numa = false    
    hotplug = "network,disk,usb"
    scsihw = "virtio-scsi-single"
    tags = "ASPOS"
    force_create = true
    network {
        bridge = "vmbr0"
        model  = "virtio"
        link_down = false
        firewall = false
    }
    os_type = "cloud-init"
    cicustom = "user=local:snippets/cloud-init.yml"
    ipconfig0 = "ip=($ip),gw=($ip)"
    nameserver = "($ip)"
    searchdomain = "($fqdn_of_domain)"
}
