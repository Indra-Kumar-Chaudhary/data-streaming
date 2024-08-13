#!/bin/bash

exec python createTables.py &
exec python makeOrders.py 
