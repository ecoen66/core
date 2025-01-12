"""Config flow to configure the CPU Speed integration."""
from __future__ import annotations

from typing import Any

from homeassistant.config_entries import ConfigFlow
from homeassistant.const import CONF_NAME
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN


class CPUSpeedFlowHandler(ConfigFlow, domain=DOMAIN):
    """Config flow for CPU Speed."""

    VERSION = 1

    _imported_name: str | None = None

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle a flow initialized by the user."""
        await self.async_set_unique_id(DOMAIN)
        self._abort_if_unique_id_configured()

        if user_input is None:
            return self.async_show_form(step_id="user")

        return self.async_create_entry(
            title=self._imported_name or "CPU Speed",
            data={},
        )

    async def async_step_import(self, config: dict[str, Any]) -> FlowResult:
        """Handle a flow initialized by importing a config."""
        self._imported_name = config.get(CONF_NAME)
        return await self.async_step_user(user_input={})
