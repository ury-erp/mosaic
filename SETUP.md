  ## URY Mosaic Setup 

Follow these steps to set up URY Mosaic after completing basic ERPNext configuration:

#### Step 1 : 

- Complete all the steps outlined in the [URY Setup](https://github.com/ury-erp/ury/blob/main/SETUP.md)

#### Step 2:

- Go to POS Profile 
- Add a naming series for KOT in "URY KOT Naming series'.
- In the Printer Info section, Configure the printer as follows: 
  - Choose network printer. 
  - Enable KOT Checkbox.
 - Note that URY Mosaic will only supports network printing . 
 - Select Print Format under "KOT Print Format Field" field.

#### Step 3:

- Create Production Unit From "URY Production Unit" with the following details:
  - **Production** : Enter the name for your Production Unit.
  - **POS Profile** : Select the POS Profile
  - **Branch** : Auto fetch when pos profile is selected 
  - **Warehouse** :Auto fetch when pos profile is selected.
  - **Item Groups** :Select Item Groups that belong to the production unit.
  - **Printers** : Table to configure printing inside production unit.
        - **Printer** : Select Network printer.
        - **KOT Print** : Enable for KOT Printing .