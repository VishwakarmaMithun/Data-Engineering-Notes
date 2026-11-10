# Author: Mithun Vishwakarma
# Date: 2026-11-11
# Version: 2.0

# Implementing the Naming Convention

A consistent naming convention is essential for data lake organization, pipeline traceability, and easy discovery across raw, processed, and curated datasets.

A common pattern is:

```text
{source}_{entity}_{YYYYMMDD}_{version}.{ext}
```

---

## Naming Pattern Breakdown

| Part | Meaning | Example |
| --- | --- | --- |
| `{source}` | Source system or ingestion channel | `sap`, `crm`, `salesforce` |
| `{entity}` | Business object or table | `customer`, `orders`, `inventory` |
| `{YYYYMMDD}` | Ingestion or snapshot date | `20261110` |
| `{version}` | Batch or file version | `v1`, `v2`, `v1.0` |
| `{ext}` | File format | `parquet`, `csv`, `json` |

### Field Descriptions

- **`{source}`**: The originating system, upstream database, or ingestion channel.
- **`{entity}`**: The dataset, table, or object being ingested.
- **`{YYYYMMDD}`**: A date format that keeps file names sortable by time.
- **`{version}`**: Tracks revisions or reruns of the same dataset.
- **`{ext}`**: The output format used for storage or downstream processing.

---

## Example File Names

### Cloud Storage Data Lake Paths

```text
gs://your-data-lake-bucket/raw/sap/customer/sap_customer_20261110_v1.parquet
gs://your-data-lake-bucket/processed/crm/orders/crm_orders_20261110_v1.0.parquet
```

These naming conventions help teams quickly understand:

- which source produced the file
- which entity or table it belongs to
- when it was created
- which version of the file is being used

---

## Python Example

```python
from datetime import datetime

source = "sap"
entity = "customer"
date_str = datetime.now().strftime("%Y%m%d")
version = "v1"
ext = "parquet"

file_name = f"{source}_{entity}_{date_str}_{version}.{ext}"
file_path = f"gs://your-data-lake-bucket/raw/{source}/{entity}/{file_name}"

print(f"Target file path: {file_path}")
```

Output example:

```text
Target file path: gs://your-data-lake-bucket/raw/sap/customer/sap_customer_20261110_v1.parquet
```

---

## Best Practices

- Keep names consistent across all ingestion pipelines.
- Use `YYYYMMDD` for date ordering and easier filtering.
- Use versioning to distinguish reprocessed or updated files.
- Prefer lowercase names and underscores for readability.
- Match the file extension to the actual stored format.
- Avoid spaces and special characters in file names.

---

## Summary

A good naming convention makes the data lake easier to manage, troubleshoot, and query. By standardizing source, entity, date, version, and extension, teams can build more reliable and scalable data pipelines.
