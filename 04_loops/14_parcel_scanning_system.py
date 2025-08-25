"""Parcel Scanning System: This is a very professional way of including for_else in code.

You are automating a parcel scanning system in a warehouse. Each parcel has a barcode. 
The system must validate all parcels and report issues:

Tasks:
    1. There is list named parcel_code which consist of barcods. 
    2. The system will go through each barcode in the list using a for loop: 
        a. If a barcode is "DAMAGED", skip it using continue and log: "Skipped damaged parcel". 
        b. If a barcode is "STOP", use break and log: "Critical error: Stopping scan". 
        c. For valid barcodes, log: "Scanned parcel: <barcode>". 
    If the loop completes without hitting a break, log: "All parcels scanned successfully" using for-else. 
    3. Return a list of all scan messages."""

# This function will be tested automatically.
# Do not change the function name or parameters.
def scan_parcels(parcel_codes: list[str]) -> list[str]:
    # Write your code below this line
    message = []
    for item in parcel_codes:
        if item == "DAMAGED":
            message.append(f"Skipped damaged parcel")
            continue
        elif item == "STOP":
            message.append(f"Critical error: Stopping scan")
            break
        else:
            message.append(f"Scanned parcel: {item}")
    
    else:
        message.append(f"All parcels scanned successfully")
        
    return message

print(f"Testcase 1: {scan_parcels(["ok", "ok", "ok", "ok", "ok"])}")
print("\n")
print(f"Testcase 2: {scan_parcels(["ok", "DAMAGED", "ok"])}")
print("\n")
print(f"Testcase 3: {scan_parcels(["ok", "DAMAGED", "ok", "STOP", "ok", "ok", "DAMAGED"])}")
print("\n")
print(f"Testcase 3: {scan_parcels(["STOP", "STOP", "STOP", "STOP", "STOP", "STOP"])}")