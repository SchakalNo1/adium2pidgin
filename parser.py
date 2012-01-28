#!/usr/bin/python
# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

from xml.dom.minidom import parse
import xml
import optparse

def parse_adium(filename):
    tree = parse(filename)
    
    chatobject = tree.childNodes[0]
    account = chatobject.getAttribute("account")
    service = chatobject.getAttribute("service")
    messages = chatobject.childNodes

    m_list = []

    for message in messages:
        if not message.nodeName == "message":
            continue

        alias = message.getAttribute("alias")
        sender = message.getAttribute("sender")
        time = message.getAttribute("time")

        child = message
        while child.nodeType != xml.dom.Node.TEXT_NODE:
            child = child.childNodes[0]

        text = child.nodeValue

        m = {"time": time, "alias": alias, "text": text, "sender": sender}
        m_list.append(m)

    c = {"messages": m_list, "account": account, "service": service}

    return c
