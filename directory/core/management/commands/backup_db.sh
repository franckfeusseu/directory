#!/bin/bash

TIME=$(date "+%s")
BACKUP_FILE="postgres_${POSTGRES_DB}_${TIME}.pgdump"
echo "Backing up $POSTGRES_DB to $BACKUP_FILE"
pg_dump --format=custom > $BACKUP_FILE
echo "Backup completed for $POSTGRES_DB"