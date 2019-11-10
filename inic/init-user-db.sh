#!/bin/bash
set -e

psql postgres -U postgres -f /root/base.sql /root/db.sql /root/usuarios.sql