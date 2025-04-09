import asyncio
import json
from datetime import datetime
from pysnmp.hlapi.v1arch.asyncio import *


async def run():
    snmpDispatcher = SnmpDispatcher() # Create a dispatcher for the get_cmd

    iterator = await get_cmd(
        snmpDispatcher,
        CommunityData("public", mpModel=0),
        await UdpTransportTarget.create(("demo.pysnmp.com", 161)), # <- Put the IP of your synology here
        ("1.3.6.1.2.1.1.1.0", None),  # sysDescr
        #("1.3.6.1.2.1.31.1.1.1.1", None),  # ifName
        #("1.3.6.1.4.1.2021.11.9.0", None),  # ssCPUuser
        #("1.3.6.1.4.1.2021.11.10.0", None),  # ssCPUsystem
        #("1.3.6.1.4.1.2021.10.1.5.3", None),  # laLoadInt3
        #("1.3.6.1.4.1.2021.4.11.0", None),  # memTotalFree
        #("1.3.6.1.4.1.2021.4.13.0", None),  # memShared
    )

    errorIndication, errorStatus, errorIndex, varBinds = iterator

    result = {"timestamp": datetime.now().isoformat()}
    if errorIndication:
        result["error"] = str(errorIndication)
    elif errorStatus:
        result["error"] = "{} at {}".format(
            errorStatus.prettyPrint(),
            errorIndex and varBinds[int(errorIndex) - 1][0] or "?",
        )
    else:
        for varBind in varBinds:
            oid, value = varBind
            result[str(oid)] = str(value)

    # Print the result as JSON
    print(json.dumps(result, indent=4))

    snmpDispatcher.transport_dispatcher.close_dispatcher()


asyncio.run(run())