## Features of URY Mosaic


### KOT (Kitchen Order Ticket)

- KOT Generation:
   - KOT are generated when order is placed in the system
   - Update button in order taking and checkout in POS will trigger initial KOT

- Modified KOT :
  - Adding new item / quantity to the existing order will generate a modified KOT 
  
- Partially cancelled KOT :
  - Removing an Item / reducing quantity from existing order  will generate a Partially cancelled KOT.
 
- Cancelled KOT :
  - Created when an entire order is cancelled .
  
- KOT Comments
  -Can attach item-wise and order-level comments to KOTs, visible in the Kitchen Display System (KDS)
  
### Production Units 

- Production units are used to rule multiple kitchens.
- Each production unit has its own dedicated web-based interface, displaying specific items.
- Printers can be configured separately for each production unit.
- KDS displays are organised by these units , access KDS via 
    `/URYMosaic/<URY_Production_Unit>`   
    
### KOT Display

 - KDS make easy to monitor kitchen orders (KOTs) on a screen..
 - Receive real-time updates for new KOTs and table changes.
 - KOTs are displayed as cards with the following details ,
   - Order Type (Table or Takeaway).
   - Table name for table orders.
   - User who placed the order
   - POS Invoice ID as Order ID.
   - KOT Created Time 
   - Item name , quantity and item wise comments.
   - Order-level comments.
   - Display available quantity and old quantity for canceled orders. 
- Ability to mark items as served and unserved.
- Timer against KOT are set in "KOT Warning Time" field within the POS profile to trigger a warning when it's exceeded. 
- Can Enable "Notify KOT Delay" for KOT delay notification feature in the POS profile and add recipients roles to the Recipients table.
- Can Enable 'KOT Audio Alert' to play a sound when a KOT is displayed. You can add an audio alert in the 'KOT alert sound' attachment field
- For Cancelled order , card display available quantity and old quantity.
- Clicking outside the items section on a KOT card reveals two buttons:
    - "Serve"  : Remove Card from the KDS and mark Serve time in KOT document.
    - "Confirm" (only for canceled KOTs): Confirms the cancellation..
    - Clicking on the card again returns to the original view.
- KOTs are color-coded for easy identification:
    - White : New KOT for table orders
    - Blue : New KOT for takeaway orders
    - Orange : Modified KOT orders
    - Red : Cancelled or partially cancelled KOT orders

### KOT Print

- Generate physical copies of KOTs
- KOT Prints are generated when order are placed
- Configure printers through network printing in POS profiles for global printing 
- To print KOT in production unit you need to configure printer in production unit separately