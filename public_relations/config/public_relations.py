from __future__ import unicode_literals
from frappe import _

def get_data():
        return [
                {
                        "label": _("Public Relations Forms"),
                        "icon": "fa fa-star",
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Agreement",
                                        "description": _("Agreement"),
                                },
                                {
                                        "type": "doctype",
                                        "name": "Incoming Letter",
                                        "description": _("Incoming Letter"),
                                },
                                {
                                        "type": "doctype",
                                        "name": "Outgoing Letters",
                                        "description": _("Outgoing Letters"),
                                },
                                {
                                        "type": "doctype",
                                        "name": "Media",
                                        "description": _("Media"),
                                },
                                {
                                        "type": "doctype",
                                        "name": "Media Cliping",
                                        "description": _("Media Cliping"),
                                },
                        ]
                },
		]
