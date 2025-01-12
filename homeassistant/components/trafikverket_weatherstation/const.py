"""Adds constants for Trafikverket Weather integration."""
from homeassistant.const import Platform

DOMAIN = "trafikverket_weatherstation"
CONF_STATION = "station"
PLATFORMS = [Platform.SENSOR]
ATTRIBUTION = "Data provided by Trafikverket"
ATTR_MEASURE_TIME = "measure_time"
ATTR_ACTIVE = "active"
