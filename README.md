# 6river
6River client

#### Sending a PickWave message

```python
from sixriver import SixRiverClient, messages as sixr_messages, models as sixr_models

picks = [
    sixr_models.Pick(
        pick_id='test-pick-id,
        group_type=sixr_models.GroupType.ORDER_PICK,
        group_id='test-group-id,
        source_location='locaiton-id',
        each_quantity=1,
        product=sixr_models.Product(
            id='product-id',
            name='test name,
            description='test description',
            unit_of_measure="instances",
            unit_of_measure_quantity=1,
            dimension_unit_of_measure="inches",
            weight_unit_of_measure="oz",
            length='1.0,
            width='1.0
            height='1.0,
            weight='1.0',
            identifiers=[
                sixr_models.Identifier(
                    label="barcode",
                    allowed_values=[
                        'some barcode',
                    ]
                ),
            ]
        ),
        data={},
        )    
    )
]

pickwave = sixr_messages.PickWaveMessage(*picks)

try:
    res = self._client.send(pickwave)
except Exception as e:
    print(e)
```
