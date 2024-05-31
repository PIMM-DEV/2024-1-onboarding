/*
직접 해보기

유니티에서 아래 코드를 적용한 큐브는 일정한 속도로 공중으로 떠오른다.

아래 코드를 적절하게 수정하여 큐브가 중력을 받아 떨어지는 것처럼 수정해보자.

* 편의상 1FPS로 동작하는 게임이라고 생각한다.
  (즉, Update()는 매 초 1회 호출된다.)
*/

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public const double G = 9.8;  // 중력가속도 G

public class CubeController : MonoBehaviour
{
    public double currentSpeed = 0;

    void Update()
    {
        transform.position = new Vector3(
            transform.position.x,
            transform.position.y + currentSpeed,
            transform.position.z
        );
        currentSpeed += G;
    }
}
