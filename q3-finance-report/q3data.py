# TGFB cash flow, Jul/Aug/Sep 2026 — Total column (Maybank + RHB) from the latest monthly
# statements (July xlsx export, August -18, September -18).
MONTHS = ["Jul-26", "Aug-26", "Sep-26"]

RECEIPTS = [
    ("Customers & Sales",        [8815311.78, 9420302.14, 9459935.84]),
    ("Licensing fee & package",  [0.00, 10000.00, 320000.00]),
    ("Royalty",                  [369866.18, 327715.27, 296844.55]),
    ("Other operations",         [42221.20, 41533.15, 42836.78]),
]
RECEIPTS_TOTAL = [9227399.16, 9799550.56, 10119617.17]

PAID = [  # positive = cash out
    ("Inventory purchases",          [4918792.44, 5000785.79, 4224003.99]),
    ("Distribution Fee",             [0.00, 0.00, 187370.00]),
    ("Deposit",                      [140976.35, 32000.00, 227765.00]),
    ("HQ Operation",                 [139925.45, 218053.87, 278274.58]),
    ("Operation",                    [0.00, 0.00, 0.00]),
    ("Marketing",                    [10638.63, 33472.90, 6945.85]),
    ("Profit sharing",               [58018.61, 114075.02, 67013.90]),
    ("Wage expenses",                [1715948.15, 1766216.42, 1760159.92]),
    ("Bank Charges",                 [148.72, 165.50, 169.80]),
    ("Income taxes",                 [250000.00, 250000.00, 250000.00]),
    ("New Branches Expenses",        [119159.11, 49573.64, 15228.00]),
    ("Branch Expenditure & Upkeep",  [148787.27, 153682.35, 155855.60]),
    ("Credit Card",                  [68504.89, 4045.97, 102185.69]),
    ("Open House & Iftar",           [0.00, 0.00, 0.00]),
    ("Co Trip",                      [0.00, 21997.70, 0.00]),
    ("Utilities",                    [170789.50, 194914.84, 182900.50]),
    ("Rental",                       [407130.32, 440962.95, 460291.05]),
    ("Sponsorship",                  [2500.00, 0.00, 0.00]),
    ("SST",                          [1031025.61, 0.00, 1152543.60]),
    ("Donation",                     [0.00, 0.00, 0.00]),
]
NET_OPS = [45054.11, 1519603.61, 1048909.69]

INVESTING = [  # signed
    ("Proceeds from sale of motor vehicle",   [190125.00, 0.00, 0.00]),
    ("Interest received (Maybank pooled)",    [0.00, 0.00, 8970.22]),
    ("Collection of Investor funds",          [0.00, 0.00, 0.00]),
    ("Sale of investment securities",         [0.00, 0.00, 0.00]),
    ("Purchase of property and equipment",    [-100223.00, -17369.00, -14400.00]),
    ("Capex New Branches",                    [-2300748.36, -402958.69, -639849.95]),
    ("Placement of Fixed Deposit",            [0.00, 0.00, -2000000.00]),
    ("Purchase of investment",                [-286293.00, 0.00, 0.00]),
]
NET_INV = [-2497139.36, -420327.69, -2645279.73]

FINANCING = [  # signed
    ("Issuance of stock",                [0.00, 0.00, 0.00]),
    ("Loan received",                    [0.00, 0.00, 0.00]),
    ("Collection of Investor funds",     [720000.00, 0.00, 229000.00]),
    ("Borrowing",                        [0.00, 0.00, 0.00]),
    ("Repayment from related parties",   [0.00, 210691.35, 8189.42]),
    ("Repayment of loans",               [-159745.15, -155237.00, -159887.29]),
    ("Dividends",                        [0.00, 0.00, 0.00]),
    ("Advance to related parties",       [-417714.58, -417.93, -201003.06]),
    ("Repayment to related parties",     [0.00, 0.00, 0.00]),
    ("Pending",                          [0.00, 0.00, 0.00]),
]
NET_FIN = [142540.27, 55036.42, -123700.93]

NET_CASH = [-2309544.98, 1154312.34, -1720070.97]
OPENING = [15448390.63, 13138845.65, 14293157.99]
CLOSING = [13138845.65, 14293157.99, 12573087.02]
