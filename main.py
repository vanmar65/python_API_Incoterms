# if you want to run this API first start the local server with
# >pip install "fastapi[all]"
# this next command starts the server
# >uvicorn main:app --reload
# some ideas to improve
# 1. put text in separate file
# add shipping method as parameter
# add table with risks
# add variable parameter
# ad info over changes between 2010 and 2020
# publish thi on external website

from fastapi import FastAPI

app = FastAPI()

I_Intro = """The Incoterms or International Commercial Terms are a series of pre-defined commercial terms published by the International Chamber of Commerce (ICC) relating to international commercial law.[1] Incoterms define the responsibilities of exporters and importers in the arrangement of shipments and
the transfer of liability involved at various stages of the transaction.
They are widely used in international commercial transactions or procurement processes and their use is encouraged by trade councils, courts and international lawyers.[2] A series of three-letter trade terms related to common contractual sales practices, the Incoterms rules are intended primarily to clearly communicate the tasks, costs, and risks associated with the
global or international transportation and delivery of goods. Incoterms inform sales contracts defining respective obligations, costs, and risks involved in the delivery of goods from the seller to the buyer, but they do not themselves conclude a contract, determine the price payable, currency or credit terms, govern contract law or define where title to goods transfers
The Incoterms rules are accepted by governments, legal authorities, and practitioners worldwide for the interpretation of most commonly used terms in international trade. They are intended to reduce or remove altogether uncertainties arising from the differing interpretations of the rules in different countries. As such they are regularly incorporated into sales contracts worldwide.[3]
'Incoterms' is a registered trademark of the ICC.The first work published by the ICC on international trade terms was issued in 1923, with the first edition known as Incoterms published in 1936. The Incoterms rules were amended in 1953,[4] 1967, 1976, 1980, 1990, 2000, and 2010, with the ninth version — Incoterms 2020 [5] — having been published on September 10, 2019."""


I_FCA = """FCA – Free Carrier (named place of delivery) The seller delivers the goods, cleared for export, at a named place (possibly including seller's own premises). The goods can be delivered to a carrier nominated by the buyer, or to another party nominated by the buyer.
In many respects this Incoterm has replaced FOB in modern usage, although the critical point at which the risk passes moves from loading aboard the vessel to the named place. The chosen place of delivery affects the obligations of loading and unloading the goods at that place.
If delivery occurs at the seller's premises, or at any other location that is under the seller's control, the seller is responsible for loading the goods on to the buyer's carrier. However, if delivery occurs at any other place, the seller is deemed to have delivered the goods once their transport has arrived at the named place; the buyer is responsible for both unloading the goods and loading them onto their own carrier."""

I_EXW = """EXW – Ex Works (named place of delivery) The seller makes the goods available at their premises, or at another named place. This term places the maximum obligation on the buyer and minimum obligations on the seller. The Ex Works term is often used while making an initial quotation for the sale of goods without any costs included. 
EXW means that a buyer incurs the risks of bringing the goods to their final destination. Either the seller does not load the goods on collecting vehicles and does not clear them for export, or if the seller does load the goods, they do so at buyer('s risk and cost. If the parties agree that the seller should be responsible for the loading of the goods on departure and to bear the risk and all costs of
such loading, this must be made clear by adding explicit wording to this effect in the contract of sale.) There is no obligation for the seller to make a contract of carriage, but there is also no obligation for the buyer to arrange one either - the buyer may sell the goods on to their own customer for collection from the original seller's warehouse. However, in common practice the buyer arranges 
the collection of the freight from the designated location, and is responsible for clearing the goods through Customs. The buyer is also responsible for completing all the export documentation, although the seller does have an obligation to obtain information and documents at the buyer's request and cost.
These documentary requirements may result in two principal issues. Firstly, the stipulation for the buyer to complete the export declaration can be an issue in certain jurisdictions (not least the European Union) where the customs regulations require the declarant to be either an individual or corporation resident within the jurisdiction. If the buyer is based outside of the customs jurisdiction, 
they will be unable to clear the goods for export, meaning that the goods may be declared in the name of the seller by the buyer, even though the export formalities are the buyer's responsibility under the EXW term.[13] Secondly, most jurisdictions require companies to provide proof of export for tax purposes. In an EXW shipment, the buyer is under no obligation to provide such proof to the seller,
or indeed to even export the goods. In a customs jurisdiction such as the European Union, this would leave the seller liable to a sales tax bill as if the goods were sold to a domestic customer. It is therefore of utmost importance that these matters are discussed with the buyer before the contract is agreed. It may well be that another Incoterm, such as FCA seller's premises, may be more suitable, 
since this puts the onus for declaring the goods for export onto the seller, which provides for more control over the export process."""

I_CPT = """CPT – Carriage Paid To (named place of destination)
CPT replaces the C&F (cost and freight) and CFR terms for all shipping modes outside of non-containerized seafreight.
The seller pays for the carriage of the goods up to the named place of destination. However, the goods are considered to be delivered when the goods have been handed over to the first or main carrier, so that the risk transfers to buyer upon handing goods over to that carrier at the place of shipment in the country of Export.
The seller is responsible for origin costs including export clearance and freight costs for carriage to the named place of destination (either the final destination such as the buyer's facilities or a port of destination. This has to be agreed to by seller and buyer, however).
If the buyer requires the seller to obtain insurance, the Incoterm CIP should be considered instead."""

I_CIP = """CIP – Carriage and Insurance Paid to (named place of destination)
This term is broadly similar to the above CPT term, with the exception that the seller is required to obtain insurance for the goods while in transit. CIP requires the seller to insure the goods for 110% of the contract value under Institute Cargo Clauses (A) of the Institute of London Underwriters (which is a change from Incoterms 2010 where the minimum was Institute Cargo Clauses (C)), or any similar set of clauses, unless specifically agreed by both parties. The policy should be in the same currency as the contract, and should allow the buyer, the seller, and anyone else with an insurable interest in the goods to be able to make a claim.
CIP can be used for all modes of transport, whereas the Incoterm CIF should only be used for non-containerized sea-freight."""


@app.get('/')
async def root():
   return{'Incoterms 2020': "2020", 'Intro': I_Intro}

@app.get('/ALL')
async def ALL():
    return{'Incoterms 2020': "2020","Intro": I_Intro,"EXW": I_EXW, 'FCA': I_FCA, "CPT": I_CPT, "CIP": I_CIP}

@app.get('/EXW')
async def EXW():
    return{'Incoterms 2020': "2020",'EXW': I_EXW}

@app.get('/FCA')
async def FCA():
    return{'Incoterms 2020': "2020",'FCA': I_FCA}

@app.get('/CPT')
async def CPT():
    return{'Incoterms 2020': "2020",'CPT': I_CPT}

@app.get('/CIP')
async def CIP():
    return{'Incoterms 2020': "2020",'CIP': I_CIP}

