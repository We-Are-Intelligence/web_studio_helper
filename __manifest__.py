{
    "name": "Studio Helper",
    "version": "19.0.1.0.0",
    "category": "Technical",
    "summary": "Power-user tools for managing and cleaning up Odoo Studio customizations",
    "description": """
Studio Helper
=============

Provides power users with:

* Quick-access menu items for Studio-created models, fields, views, and metadata.
* Automated cleanup of ``ir.model.data`` references when Studio models or fields
  are deleted — preventing the infamous *"Missing Record"* errors during
  Studio customisation uninstallation.
    """,
    "author": "",
    "website": "",
    "license": "LGPL-3",
    "depends": [
        "base_automation",
    ],
    "data": [
        "data/server_actions.xml",
        "data/window_actions.xml",
        "data/automations.xml",
        "views/menus.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}