---
type: regex
target: last_message
pattern: 'serviceusage\.serviceUsageConsumer|Service Usage Consumer'
flags: i
---
Setting a quota project requires the `serviceusage.services.use` permission, granted by `roles/serviceusage.serviceUsageConsumer` (or a broader role that includes it, such as Editor/Owner) on the target project.
