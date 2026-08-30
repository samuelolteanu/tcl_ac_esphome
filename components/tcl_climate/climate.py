import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import climate, uart, sensor
from esphome.const import CONF_ID, CONF_SENSOR

CONF_HUMIDITY_SENSOR = "humidity_sensor"

DEPENDENCIES = ['uart']
AUTO_LOAD = ['climate']

tcl_climate_ns = cg.esphome_ns.namespace('tcl_climate')
TCLClimate = tcl_climate_ns.class_('TCLClimate', climate.Climate, uart.UARTDevice, cg.PollingComponent)

CONFIG_SCHEMA = climate.climate_schema(TCLClimate).extend({
    cv.GenerateID(): cv.declare_id(TCLClimate),
    cv.Optional(CONF_SENSOR): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_HUMIDITY_SENSOR): cv.use_id(sensor.Sensor),
}).extend(uart.UART_DEVICE_SCHEMA).extend(cv.polling_component_schema('450ms'))

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await climate.register_climate(var, config)
    await uart.register_uart_device(var, config)

    if CONF_SENSOR in config:
        sens = await cg.get_variable(config[CONF_SENSOR])
        cg.add(var.set_temperature_sensor(sens))

    if CONF_HUMIDITY_SENSOR in config:
        hsens = await cg.get_variable(config[CONF_HUMIDITY_SENSOR])
        cg.add(var.set_humidity_sensor(hsens))
