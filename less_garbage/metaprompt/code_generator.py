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

### example script
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
Each script you generate should follow this structure, with the name "Generation". Add any additional logic specific to the particular script's functionality.
'''