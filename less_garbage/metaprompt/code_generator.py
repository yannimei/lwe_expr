metaprompt = '''
You are tasked with generating C# scripts for Unity that adhere to the following interface:

### interface
public interface ChatGPTScript
{
    public string GetName();          // Returns the name of the script
    public void DestroyScript();      // Destroys the script instance
    public void SetActive(bool active); // Sets the script's active state
    public bool GetActive();          // Returns the active state (enabled/disabled)
    public ScriptParamData[] GetParams(); //create parameter
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
        Destroy(this);
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

If the script includes numerical parameters such as speed, range, or any similar value:
- Store them as independent variables.
- Create get and set methods for each parameter.
- Generate a ScriptParamData[] array containing an entry for each parameter, and return it in the GetParams() function. 
- To note, ScriptParamData is a predefined Struct, containing name, get and set function for a parameter, the code is shown:
### Struct
public struct ScriptParamData
{
    public string name;           // The name of the parameter
    public Func<float> Get;       // A function to get the parameter's value
    public Action<float> Set;     // A function to set the parameter's value

    public ScriptParamData(string name, Func<float> Get, Action<float> Set)
    {
        this.name = name;
        this.Get = Get;
        this.Set = Set;
    }
}

Here is the example of script for two parameters for speed and range:

### example script 3
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Generation : MonoBehaviour, ChatGPTScript
{
    // Public float variables for parameters like speed and range
    public float speed;
    public float range;

    // Method to set the speed variable
    public void SetSpeed(float speed) 
    { 
        this.speed = speed; // Assign the passed value to the speed field
    }

    // Method to get the current speed value
    public float GetSpeed() 
    {
        return speed; // Returns the current value of speed
    }
    
    // Method to set the range variable
    public void SetRange(float range) 
    { 
        this.range = range; // Assign the passed value to the range field
    }

    // Method to get the current range value
    public float GetRange() 
    {
        return range; // Returns the current value of range
    }

    public void DestroyScript()
    {
        Destroy(this);
    }

    public bool GetActive()
    {
        return this.enabled;
    }

    public string GetName()
    {
        return "scriptname";
    }

    // Method that returns an array of ScriptParamData to expose parameters
    public ScriptParamData[] GetParams()
    {
        // Links speed and range with their Get and Set methods
        return new ScriptParamData[] {new ScriptParamData("speed", this.GetSpeed, this.SetSpeed), new ScriptParamData("range", this.GetRange, this.SetRange)};
    }

    public void SetActive(bool active)
    {
        this.enabled = active;
    }
}

Each script you generate should follow this structure, with the name "Generation". Add any additional logic specific to the particular script's functionality.

'''