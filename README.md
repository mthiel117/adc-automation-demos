# Automation Examples for Arista Demo Cloud (ADC)

### 1. Create configlets from CSV

```
ansible-playbook create-configlets-from-csv.yml
```

### 2. Backup running-config on each device to ./config_backup

```
ansible-playbook backup-configs.yml
```

### 3. Upload configlets to CVP from directory ./configlets

This step MUST be completed before moving to Step 4, as the configlets need to be in CVP before running the playbook in Step 4.

```
ansible-playbook configlet-uploader.yml
```
or you can run a Python script to do the same work
```
./pushconfigs_to_cvp.py

```

### 4. Bind Configlets to single device dc1-poe-leaf-sw1
Makes use of Tags to provision or rollback changes to the device.  Static list of configlets are defined in the playbook.  After each playbook is run you must go into CVP and execute the Task created for 'leaf1'.

```
ansible-playbook device-configlets.yml --tags provision

ansible-playbook device-configlets.yml --tags rollback

```