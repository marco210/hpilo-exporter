from prometheus_client import Gauge
from prometheus_client import REGISTRY

registry = REGISTRY

hpilo_system_health_gauge = Gauge('hpilo_system_health','{0: OK, 1: Warning, 2: Critical}',['bios_version','server_model','power_state','bios_backup','os_name','os_description','intelligent_provisioning_version','pca_part_number','post_state','sku','serial_number'])

hpilo_processors_status_gauge = Gauge('hpilo_processors_status','{0: OK, 1: Warning, 2: Critical}')
hpilo_power_supply_redundancy_status_gauge = Gauge('hpilo_power_supply_redundancy_status','{0: Redundant, 2: FailedRedundant, NonRedundant, Unknown}')
hpilo_power_supplies_status_gauge = Gauge('hpilo_power_supplies_status','{0: OK, 1: Warning, 2: Critical}')
hpilo_storages_status_gauge = Gauge('hpilo_storages_status','{0: OK, 1: Warning, 2: Critical}')
hpilo_fan_redundancy_status_gauge = Gauge('hpilo_fan_redundancy_status','{0: Redundant, 2: FailedRedundant, NonRedundant, Unknown}')
hpilo_fans_status_gauge = Gauge('hpilo_fans_status','{0: OK, 1: Warning, 2: Critical}')
hpilo_temperatures_status_gauge = Gauge('hpilo_temperatures_status','{0: OK, 1: Warning, 2: Critical}')
hpilo_memories_status_gauge = Gauge('hpilo_memories_status','{0: OK, 1: Warning, 2: Critical}')
hpilo_bios_or_hardware_health_status_gauge = Gauge('hpilo_bios_or_hardware_health_status','{0: OK, 1: Warning, 2: Critical}')
hpilo_networks_status_gauge = Gauge('hpilo_networks_status','{0: OK, 1: Warning, 2: Critical}')
hpilo_agentless_management_service_status_gauge = Gauge('hpilo_agentless_management_service_status','{0: Ready, 2: Unavailable}')
hpilo_smart_storage_batteries_status_gauge = Gauge('hpilo_smart_storage_batteries_status','{0: OK, 1: Warning, 2: Critical}')

status_gauges = {
    'hpilo_processors_status_gauge': hpilo_processors_status_gauge,
    'hpilo_power_supply_redundancy_status_gauge': hpilo_power_supply_redundancy_status_gauge,
    'hpilo_power_supplies_status_gauge': hpilo_power_supplies_status_gauge,
    'hpilo_storages_status_gauge': hpilo_storages_status_gauge,
    'hpilo_fan_redundancy_status_gauge': hpilo_fan_redundancy_status_gauge,
    'hpilo_fans_status_gauge': hpilo_fans_status_gauge,
    'hpilo_temperatures_status_gauge': hpilo_temperatures_status_gauge,
    'hpilo_memories_status_gauge': hpilo_memories_status_gauge,
    'hpilo_bios_or_hardware_health_status_gauge': hpilo_bios_or_hardware_health_status_gauge,
    'hpilo_networks_status_gauge': hpilo_networks_status_gauge,
    'hpilo_agentless_management_service_status_gauge': hpilo_agentless_management_service_status_gauge,
    'hpilo_smart_storage_batteries_status_gauge': hpilo_smart_storage_batteries_status_gauge
}

hpilo_memorybusutil_gauge = Gauge('hpilo_memorybusutil','Current System memory bus utilization in percentage.')
hpilo_avgcpu0freq_gauge = Gauge('hpilo_avgcpu0freq','Current CPU0 average frequency in MHz.')
hpilo_jittercount_gauge = Gauge('hpilo_jittercount','Current processor Jitter Count.')
hpilo_cpuutil_gauge = Gauge('hpilo_cpuutil','Current System CPU utilization in percentage.')
hpilo_avgcpu1freq_gauge = Gauge('hpilo_avgcpu1freq','Current CPU1 average frequency in MHz.')
hpilo_iobusutil_gauge = Gauge('hpilo_iobusutil','Current System I/O bus utilization in percentage.')
hpilo_cpuicutil_gauge = Gauge('hpilo_cpuicutil','Current System CPU Interconnect utilization in percentage.')
hpilo_cpu0power_gauge = Gauge('hpilo_cpu0power','Current power consumed by the system CPU0 in Watts.')
hpilo_cpu1power_gauge = Gauge('hpilo_cpu1power','Current power consumed by the system CPU1 in Watts.')

system_usage_gauges = {
    'hpilo_memorybusutil_gauge': hpilo_memorybusutil_gauge,
    'hpilo_avgcpu0freq_gauge': hpilo_avgcpu0freq_gauge,
    'hpilo_jittercount_gauge': hpilo_jittercount_gauge,
    'hpilo_cpuutil_gauge': hpilo_cpuutil_gauge,
    'hpilo_avgcpu1freq_gauge': hpilo_avgcpu1freq_gauge,
    'hpilo_iobusutil_gauge': hpilo_iobusutil_gauge,
    'hpilo_cpuicutil_gauge': hpilo_cpuicutil_gauge,
    'hpilo_cpu0power_gauge': hpilo_cpu0power_gauge,
    'hpilo_cpu1power_gauge': hpilo_cpu1power_gauge
}

hpilo_array_controller_status_gauge = Gauge('hpilo_array_controller_status','{0: OK, 1: Warning, 2: Critical}',['id','location','model','unconfigured_drives','internal_port_count','backup_power_source_status','part_number','controller_board','current_operating_mode','read_cache_percent','firmware_version'])

hpilo_logical_drive_status_gauge = Gauge('hpilo_logical_drive_status','{0: OK, 1: Warning, 2: Critical}',['id_array','id','capacity','media_type','raid','physical_drive_id','logical_drive_status_reasons','interface_type','logical_drive_type','acceleration_method'])

hpilo_physical_drive_status_gauge = Gauge('hpilo_physical_drive_status','{0: OK, 1: Warning, 2: Critical}',['id','location','capacity','media_type','model','id_array','interface_type','carrier_authentication_status','disk_drive_use','interface_speed_mbps','disk_drive_status_reasons','firmware_version','rotational_speed_rpm'])

hpilo_physical_drive_metrics_gauge = Gauge('hpilo_physical_drive_metrics','Metrics of physical drive',['id','maximum_recommended','power_on_hours','ssd_endurance','uncorrected_read_errors','uncorrected_write_errors','current_temperature'])

hpilo_physical_drive_power_on_hours_gauge = Gauge('hpilo_physical_drive_power_on_hours','The number of lifetime hours that the drive has been powered on. The value is null if the disk power on hours cannot be determined or is not supported.',['id','location','capacity','media_type','model','id_array','interface_type','interface_speed_mbps'])

hpilo_physical_drive_ssd_endurance_gauge = Gauge('hpilo_physical_drive_ssd_endurance','This is the percentage of the drive that has been worn out and can no longer be used. When this values reaches 100%, the drive has 0% usage remaining and is completely worn out. The value is null if percent endurance used cannot be determined or is not supported.',['id','location','capacity','media_type','model','id_array','interface_type','interface_speed_mbps'])

hpilo_physical_drive_uncorrected_read_errors_gauge = Gauge('hpilo_physical_drive_uncorrected_read_errors','The number of read errors that have occurred on a drive that could not be recovered, If an increase in this counter is seen, run diagnostics on the drive',['id','location','capacity','media_type','model','id_array','interface_type','interface_speed_mbps'])

hpilo_physical_drive_uncorrected_write_errors_gauge = Gauge('hpilo_physical_drive_uncorrected_write_errors','The number of write errors that have occurred on a drive that could not be recovered, If an increase in this counter is seen, run diagnostics on the drive',['id','location','capacity','media_type','model','id_array','interface_type','interface_speed_mbps'])

hpilo_storage_enclosure_status_gauge = Gauge('hpilo_storage_enclosure_status','{0: OK, 1: Warning, 2: Critical}',['id','location_identifier','model','id_array','drive_bays_supported','firmware_version'])

hpilo_memory_status_gauge = Gauge('hpilo_memory_status','{0: OK, 1: Warning, 2: Critical}',['location','channel','module_status','part_number','capacity','device_type','operating_speed_mhz'])

hpilo_processor_status_gauge = Gauge('hpilo_processor_status','{0: OK, 1: Warning, 2: Critical}',['id','model','caches','cores_threads','last_boot_speed','max_speed_supported','cores_enabled'])

hpilo_smart_storage_battery_status_gauge = Gauge('hpilo_smart_storage_battery_status','{0: OK, 1: Warning, 2: Critical}',['id','charge_level_percent','maximum_capacity_watts','model','remaining_charge_time_seconds','spare_part_number','firmware_version'])

hpilo_smart_storage_battery_charge_level_percent_gauge = Gauge('hpilo_smart_storage_battery_charge_level_percent','',['id','model','spare_part_number','firmware_version'])

hpilo_power_consumed_by_all_gauge = Gauge('hpilo_power_consumed_by_all','The actual power being consumed by the server in Watts',['id','capacity'])

hpilo_power_control_gauge = Gauge('hpilo_power_control','',['id','capacity','max_consumed','min_consumed','average_consumed','interval_in_min'])

hpilo_power_consumed_by_each_gauge = Gauge('hpilo_power_consumed_by_each','The latest observed average power being drawn by the power supply (Watts)',['id','capacity','model','location'])

hpilo_power_line_input_voltage_gauge = Gauge('hpilo_power_line_input_voltage','The line input voltage at which the Power Supply is operating',['id','capacity','model','location'])

hpilo_power_supply_status_gauge = Gauge('hpilo_power_supply_status','{0: OK, 1: Warning, 2: Critical}',['id','capacity','model','location','hot_plug_capable','power_supply_status','max_output_watts_10s_interval','spare_part_number','firmware_version'])

hpilo_fan_speed_gauge = Gauge('hpilo_fan_speed','The current speed of the fan',['id','name','hot_pluggable','cool_location'])

hpilo_fan_status_gauge = Gauge('hpilo_fan_status','{0: OK, 1: Warning, 2: Critical}',['id','name','hot_pluggable','cool_location'])

hpilo_temperature_reading_gauge = Gauge('hpilo_temperature_reading','The current reading of the temperature sensor in Celsius',['id','name','location','caution','critical'])

hpilo_temperature_reading_status_gauge = Gauge('hpilo_temperature_reading_status','{0: OK, 1: Warning, 2: Critical}',['id','name','location','caution','critical','temperature'])

hpilo_network_adapter_status_gauge = Gauge('hpilo_network_adapter_status','{0: OK, 1: Warning, 2: Critical}',['id','name','part_number','firmware_version'])

hpilo_network_port_bad_receives_gauge = Gauge('hpilo_network_port_bad_receives','A count of frames that were received by the adapter but which had an error',['id_adapter','name_adapter','port_number','full_duplex','ipv4_addresses','link_status','name','speed_mbps','team','mac_address'])

hpilo_network_port_bad_transmits_gauge = Gauge('hpilo_network_port_bad_transmits','A count of frames that were not transmitted by the adapter because of an error',['id_adapter','name_adapter','port_number','full_duplex','ipv4_addresses','link_status','name','speed_mbps','team','mac_address'])

hpilo_network_port_good_receives_gauge = Gauge('hpilo_network_port_good_receives','A count of frames successfully received by the physical adapter',['id_adapter','name_adapter','port_number','full_duplex','ipv4_addresses','link_status','name','speed_mbps','team','mac_address'])

hpilo_network_port_good_transmits_gauge = Gauge('hpilo_network_port_good_transmits','A count of frames successfully transmitted by the physical adapter',['id_adapter','name_adapter','port_number','full_duplex','ipv4_addresses','link_status','name','speed_mbps','team','mac_address'])

hpilo_network_port_status_gauge = Gauge('hpilo_network_port_status','{0: OK, 1: Warning, 2: Critical}',['id_adapter','name_adapter','port_number','full_duplex','ipv4_addresses','link_status','name','speed_mbps','team','mac_address'])

hpilo_ilo_port_status_gauge = Gauge('hpilo_ilo_port_status','{0: OK, 1: Warning, 2: Critical}',['full_duplex','address','address_origin','gateway','subnet_mask','interface_enabled','interface_type','speed_mbps'])

