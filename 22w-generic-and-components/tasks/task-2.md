# Task 2

[doc-2.pdf](./doc-2.pdf)를 읽고 아래 두 코드가 서로 상호작용할 수 있도록 코드를 한 줄 추가하시오.  

* 게임 실행 시 PlayerController.cs 파일에서 `ListManager.coins`에 정수 `3`, `4`, `5` 추가

ListManager.cs
```csharp
using UnityEngine;
using System.Collections;

public class ListManager : MonbBehaviour
{
    public GameObject otherObject;
    PlayerController playerController;
    public List<int> coins;

    void Awake()
    {
        playerController = otherObject.GetComponent<PlayerController>();
    }
}
```

PlayerController.cs
```csharp
using UnityEngine;
using System.Collections;

public class PlayerController : MonoBehaviour
{
    public GameObject otherObject;
    ListManager listManager;

    void Awake()
    {
        listManager = otherObject.GetComponent<ListManager>();
    }

    void Start()
    {
    }
}
```
