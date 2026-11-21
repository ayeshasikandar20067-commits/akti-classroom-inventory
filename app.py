
import gradio as gr
import os
inventory = {
    101: {"item": "Computer", "quantity": 20, "condition": "Good"},
    102: {"item": "Chair", "quantity": 25, "condition": "Good"},
    103: {"item": "Table", "quantity": 10, "condition": "Good"},
    104: {"item": "Projector", "quantity": 1, "condition": "Good"},
    105: {"item": "Whiteboard", "quantity": 2, "condition": "Good"},
    106: {"item": "Fan", "quantity": 4, "condition": "Good"},
    107: {"item": "Air Conditioner", "quantity": 2, "condition": "Good"},
    108: {"item": "Lights", "quantity": 8, "condition": "Good"}
}

def view_items():
    return [
        [id, item["item"], item["quantity"], item["condition"]]
        for id, item in inventory.items()
    ]

def add_item(item_id, name, qty, condition):
    item_id = int(item_id)
    inventory[item_id] = {
        "item": name,
        "quantity": int(qty),
        "condition": condition
    }
    return "Item Added Successfully!"

def search_item(item_id):
    item_id = int(item_id)
    if item_id in inventory:
        item = inventory[item_id]
        return [[item_id, item["item"], item["quantity"], item["condition"]]]
    return [["Not Found", "", "", ""]]

def update_item(item_id, qty, condition):
    item_id = int(item_id)
    if item_id in inventory:
        inventory[item_id]["quantity"] = int(qty)
        inventory[item_id]["condition"] = condition
        return "Item Updated Successfully!"
    return "Item Not Found!"

with gr.Blocks() as demo:
    gr.Markdown("# AKTI Classroom Inventory Management System")

    gr.Markdown("### View Items")
    view_btn = gr.Button("View Items")
    table = gr.Dataframe(
        headers=["Item ID", "Item Name", "Quantity", "Condition"]
    )
    view_btn.click(view_items, inputs=None, outputs=table)

    gr.Markdown("### Add New Item")
    item_id = gr.Number(label="Item ID", precision=0)
    name = gr.Textbox(label="Item Name")
    qty = gr.Number(label="Quantity", precision=0)
    condition = gr.Textbox(label="Condition")
    add_btn = gr.Button("Add Item")
    message = gr.Textbox(label="Status")
    add_btn.click(add_item, [item_id, name, qty, condition], message)

    gr.Markdown("### Search Item")
    search_id = gr.Number(label="Enter Item ID", precision=0)
    search_btn = gr.Button("Search Item")
    search_table = gr.Dataframe(
        headers=["Item ID", "Item Name", "Quantity", "Condition"]
    )
    search_btn.click(search_item, search_id, search_table)

    gr.Markdown("### Update Item")
    update_id = gr.Number(label="Item ID", precision=0)
    update_qty = gr.Number(label="New Quantity", precision=0)
    update_condition = gr.Textbox(label="New Condition")
    update_btn = gr.Button("Update Item")
    update_message = gr.Textbox(label="Status")
    update_btn.click(
        update_item,
        [update_id, update_qty, update_condition],
        update_message
    )

demo.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 10000)))
