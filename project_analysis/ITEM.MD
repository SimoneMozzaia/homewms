<b>ITEM requirements</b>
<h6>2024-06-16</h6>
As a User, I want to be able to create an item that has the following characteristics:
- Unique ID
- Name
- Description
- Category
- Barcode
- Weight (in grams)
- If dangerous (f.e. Flammable)
- If fragile
- Creation Date
- Last Update Date
- Last Update User

I also want to be able to update the item and delete the item.

Implementation details can be found in:
- [models/item](/backend/models/item.py)
- [routes/item](/backend/routes/item.py)
- [schemas/item](/backend/schemas/item.py)