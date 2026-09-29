import frappe

def run():
    doc = frappe.get_doc("Navbar Settings")
    doc.settings_dropdown = []

    doc.append("settings_dropdown", {
        "item_label": "My Profile",
        "route": "/app/user-profile"
    })
    doc.append("settings_dropdown", {
        "item_label": "Settings",
        "route": "/app/workspace/Settings"
    })
    doc.append("settings_dropdown", {
        "item_label": "Reload",
        "action": "frappe.ui.toolbar.clear_cache()"
    })
    doc.append("settings_dropdown", {
        "item_label": "Toggle Theme",
        "action": "frappe.ui.toolbar.toggle_theme()"
    })
    doc.append("settings_dropdown", {
        "item_label": "Log out",
        "action": "frappe.app.logout()"
    })

    doc.save()
    frappe.db.commit()
    print("Successfully restored Navbar Settings!")
