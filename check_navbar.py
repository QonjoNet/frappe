import frappe

frappe.init(site="localhost", sites_path="/home/ulakeb/work/qonjo-lms/frappe-bench/sites")
frappe.connect()

navbar_settings = frappe.get_doc("Navbar Settings")
print("Settings Dropdown Items:")
for item in navbar_settings.settings_dropdown:
    print(f"- {item.item_label}")

print("\nHelp Dropdown Items:")
for item in navbar_settings.help_dropdown:
    print(f"- {item.item_label}")
