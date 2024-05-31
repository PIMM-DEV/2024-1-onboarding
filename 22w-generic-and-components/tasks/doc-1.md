# Unity - Scripting API: Rigidbody.rotation

**Rigidbody.rotation**

```csharp
public Quaternion rotation;
```

### **Description**

The rotation of the Rigidbody.

Use Rigidbody.rotation to get and set the rotation of a Rigidbody using the physics engine.

Changing the rotation of a Rigidbody using Rigidbody.rotation updates the Transform after the next physics simulation step. This is faster than updating the rotation using Transform.rotation, as Transform.rotation causes all attached Colliders to recalculate their rotation relative to the Rigidbody, whereas Rigidbody.rotation sets the values directly to the physics system.

If you want to continuously rotate a rigidbody use MoveRotation instead, which takes interpolation into account.

**Note:** rotation is world-space.

```csharp
using UnityEngine;
using System.Collections;

public class ExampleClass : MonoBehaviour
{
    void Start()
    {
        GetComponent<Rigidbody>().rotation = Quaternion.identity;
    }
}
```