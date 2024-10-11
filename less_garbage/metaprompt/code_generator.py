metaprompt = '''
You are tasked with generating C# scripts for Unity that adhere to the following interface:

### interface
public interface ChatGPTScript
{
    public string GetName();          // Returns the name of the script
    public void DestroyScript();      // Destroys the script instance
    public void SetActive(bool active); // Sets the script's active state
    public bool GetActive();          // Returns the active state (enabled/disabled)
}

Each generated script should:
- Inherit from both MonoBehaviour and ChatGPTScript.
- Implement the required methods defined in the ChatGPTScript interface.
- Use Unity's built-in methods where applicable (e.g., Destroy(), enabled property).


here is an example for how to implement the interface:
### example script 1
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
public class Generation: MonoBehaviour, ChatGPTScript
{
    public void DestroyScript()
    {
        Destroy(this);  // Destroys the current script instance
    }

    public bool GetActive()
    {
        return this.enabled;  // Returns the script's active state
    }

    public string GetName()
    {
        return "scriptname";  // Replace with the appropriate script name
    }

    public void SetActive(bool active)
    {
        this.enabled = active;  // Enables or disables the script
    }
}

If the script creates or instantiates any game objects, ensure the following:
- Destroy the game object in the DestroyScript() method.
- Disable or enable the game object in the SetActive() method.

Here is the example:

### example script 2
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Generation : MonoBehaviour, ChatGPTScript
{
    private GameObject cube;

    public string GetName()
    {
        return "Example";
    }

    public void DestroyScript()
    {
        Destroy(this.cube);  // Destroys the created object
        Destroy(this.gameObject);
    }

    public void SetActive(bool active)
    {
        this.cube.SetActive(active);  // Enables or disables the cube
        this.enabled = active;
    }

    private void Start()
    {
        this.cube = GameObject.CreatePrimitive(PrimitiveType.Cube);
    }
}

Each script you generate should follow this structure, with the name "Generation". Add any additional logic specific to the particular script's functionality.
'''