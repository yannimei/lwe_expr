metaprompt = '''
   You will be given a JSON file with all white spaces and quotations removed, which contains all the
game objects in a 3D Unity scene that may represent a particular object, widget, or even an
entire 3D world. Your task is to interpret this JSON file and give a brief description of the
scene.
# Guidelines
- Pay attention to the user request and only summarize the part of scene that is relevant for
fulfilling the request. For example, suppose there are a lot of objects in the scene, among which
is an apple. If the user only wants to change the color of the apple, only output information
relevant to the apple.
- Pay attention to the user request including themselves, such as "me" or "my right hand". Consider the users and their hands also game objects. The "XRRig" is me (the user). The "MainCamera" gameObject is my head (the user's). The "LeftHand" is my left hand (the user's). The "RightHand" is my left hand (the user's).For example, suppose want to move themselves to the apple, besides Apple also give output information relevant to the "me" which is XRRig.
- A child is usually a sub-component of its parent.
- The "ChatGPTTester" gameObject is a manager that contains the previously generated scripts.
- If there is a child object, list the names only. Do not mention their relationship with the parent.
- If the user mentions an arm, such as the left arm, refer to the game object of the hand on the corresponding side, such as "LeftHand."


# Examples
## Example
User:
Request: Move the apple to the table
Scene JSON: {objects:[{name:XRInteractionManager,components:[UnityEngine.Transform,UnityEngine.XR.Interaction.Toolkit.XRInteractionManager]},{name:XRRig,components:[UnityEngine.Transform,Unity.XR.CoreUtils.XROrigin,UnityEngine.XR.Interaction.Toolkit.Inputs.InputActionManager,UnityEngine.XR.Interaction.Toolkit.LocomotionSystem,UnityEngine.CharacterController,UnityEngine.XR.Interaction.Toolkit.TeleportationProvider,XROriginFloorFix]},{name:DirectionalLight,components:[UnityEngine.Transform,UnityEngine.Light]},{name:Plane,components:[UnityEngine.Transform,UnityEngine.MeshFilter,UnityEngine.MeshRenderer,UnityEngine.BoxCollider,UnityEngine.Rigidbody,UnityEngine.XR.Interaction.Toolkit.TeleportationArea]},{name:Sketchfab,components:[UnityEngine.Transform,SketchFabCall]},{name:Apple,components:[UnityEngine.Transform,UnityEngine.MeshFilter,UnityEngine.MeshRenderer,UnityEngine.SphereCollider,UnityEngine.Rigidbody,UnityEngine.XR.Interaction.Toolkit.XRGrabInteractable,UnityEngine.XR.Interaction.Toolkit.Transformers.XRGeneralGrabTransformer]},{name:Pear,components:[UnityEngine.Transform,UnityEngine.MeshFilter,UnityEngine.MeshRenderer,UnityEngine.SphereCollider,UnityEngine.Rigidbody,UnityEngine.XR.Interaction.Toolkit.XRGrabInteractable,UnityEngine.XR.Interaction.Toolkit.Transformers.XRGeneralGrabTransformer]},{name:test,components:[UnityEngine.Transform,InputTest]},{name:Table,components:[UnityEngine.Transform,UnityEngine.MeshFilter,UnityEngine.MeshRenderer,UnityEngine.BoxCollider]},{name:SketchfabWebRequestManager,components:[UnityEngine.Transform,SketchfabWebRequestManager]}]}
assistant:
Relevant objects: "Apple", "Table" .

## Example
User:
Request: Move me closed to the kiwi
Scene JSON: {objects:[{name:XRInteractionManager,components:[UnityEngine.Transform,UnityEngine.XR.Interaction.Toolkit.XRInteractionManager]},{name:XRRig,components:[UnityEngine.Transform,Unity.XR.CoreUtils.XROrigin,UnityEngine.XR.Interaction.Toolkit.Inputs.InputActionManager,UnityEngine.XR.Interaction.Toolkit.LocomotionSystem,UnityEngine.CharacterController,UnityEngine.XR.Interaction.Toolkit.TeleportationProvider,XROriginFloorFix]},{name:DirectionalLight,components:[UnityEngine.Transform,UnityEngine.Light]},{name:Plane,components:[UnityEngine.Transform,UnityEngine.MeshFilter,UnityEngine.MeshRenderer,UnityEngine.BoxCollider,UnityEngine.Rigidbody,UnityEngine.XR.Interaction.Toolkit.TeleportationArea]},{name:Sketchfab,components:[UnityEngine.Transform,SketchFabCall]},{name:Apple,components:[UnityEngine.Transform,UnityEngine.MeshFilter,UnityEngine.MeshRenderer,UnityEngine.SphereCollider,UnityEngine.Rigidbody,UnityEngine.XR.Interaction.Toolkit.XRGrabInteractable,UnityEngine.XR.Interaction.Toolkit.Transformers.XRGeneralGrabTransformer]},{name:Pear,components:[UnityEngine.Transform,UnityEngine.MeshFilter,UnityEngine.MeshRenderer,UnityEngine.SphereCollider,UnityEngine.Rigidbody,UnityEngine.XR.Interaction.Toolkit.XRGrabInteractable,UnityEngine.XR.Interaction.Toolkit.Transformers.XRGeneralGrabTransformer]},{name:test,components:[UnityEngine.Transform,InputTest]},{name:Table,components:[UnityEngine.Transform,UnityEngine.MeshFilter,UnityEngine.MeshRenderer,UnityEngine.BoxCollider]},{name:SketchfabWebRequestManager,components:[UnityEngine.Transform,SketchfabWebRequestManager]}]}
assistant:
Relevant objects: "XRRig", "Kiwi" .

## Example
User:
Request: Move my right hand to the apple
Scene JSON: {objects:[{name:XRInteractionManager,components:[UnityEngine.Transform,UnityEngine.XR.Interaction.Toolkit.XRInteractionManager]},{name:XRRig,components:[UnityEngine.Transform,Unity.XR.CoreUtils.XROrigin,UnityEngine.XR.Interaction.Toolkit.Inputs.InputActionManager,UnityEngine.XR.Interaction.Toolkit.LocomotionSystem,UnityEngine.CharacterController,UnityEngine.XR.Interaction.Toolkit.TeleportationProvider,XROriginFloorFix]},{name:DirectionalLight,components:[UnityEngine.Transform,UnityEngine.Light]},{name:Plane,components:[UnityEngine.Transform,UnityEngine.MeshFilter,UnityEngine.MeshRenderer,UnityEngine.BoxCollider,UnityEngine.Rigidbody,UnityEngine.XR.Interaction.Toolkit.TeleportationArea]},{name:Sketchfab,components:[UnityEngine.Transform,SketchFabCall]},{name:Apple,components:[UnityEngine.Transform,UnityEngine.MeshFilter,UnityEngine.MeshRenderer,UnityEngine.SphereCollider,UnityEngine.Rigidbody,UnityEngine.XR.Interaction.Toolkit.XRGrabInteractable,UnityEngine.XR.Interaction.Toolkit.Transformers.XRGeneralGrabTransformer]},{name:Pear,components:[UnityEngine.Transform,UnityEngine.MeshFilter,UnityEngine.MeshRenderer,UnityEngine.SphereCollider,UnityEngine.Rigidbody,UnityEngine.XR.Interaction.Toolkit.XRGrabInteractable,UnityEngine.XR.Interaction.Toolkit.Transformers.XRGeneralGrabTransformer]},{name:test,components:[UnityEngine.Transform,InputTest]},{name:Table,components:[UnityEngine.Transform,UnityEngine.MeshFilter,UnityEngine.MeshRenderer,UnityEngine.BoxCollider]},{name:SketchfabWebRequestManager,components:[UnityEngine.Transform,SketchfabWebRequestManager]}]}
assistant:
Relevant objects: "RightHand", "Apple" .

## Example
User:
Request: I want to extend my right arm
Scene JSON: {objects:[{name:XRInteractionManager,components:[UnityEngine.Transform,UnityEngine.XR.Interaction.Toolkit.XRInteractionManager]},{name:XRRig,components:[UnityEngine.Transform,Unity.XR.CoreUtils.XROrigin,UnityEngine.XR.Interaction.Toolkit.Inputs.InputActionManager,UnityEngine.XR.Interaction.Toolkit.LocomotionSystem,UnityEngine.CharacterController,UnityEngine.XR.Interaction.Toolkit.TeleportationProvider,XROriginFloorFix]},{name:DirectionalLight,components:[UnityEngine.Transform,UnityEngine.Light]},{name:Plane,components:[UnityEngine.Transform,UnityEngine.MeshFilter,UnityEngine.MeshRenderer,UnityEngine.BoxCollider,UnityEngine.Rigidbody,UnityEngine.XR.Interaction.Toolkit.TeleportationArea]},{name:Sketchfab,components:[UnityEngine.Transform,SketchFabCall]},{name:Apple,components:[UnityEngine.Transform,UnityEngine.MeshFilter,UnityEngine.MeshRenderer,UnityEngine.SphereCollider,UnityEngine.Rigidbody,UnityEngine.XR.Interaction.Toolkit.XRGrabInteractable,UnityEngine.XR.Interaction.Toolkit.Transformers.XRGeneralGrabTransformer]},{name:Pear,components:[UnityEngine.Transform,UnityEngine.MeshFilter,UnityEngine.MeshRenderer,UnityEngine.SphereCollider,UnityEngine.Rigidbody,UnityEngine.XR.Interaction.Toolkit.XRGrabInteractable,UnityEngine.XR.Interaction.Toolkit.Transformers.XRGeneralGrabTransformer]},{name:test,components:[UnityEngine.Transform,InputTest]},{name:Table,components:[UnityEngine.Transform,UnityEngine.MeshFilter,UnityEngine.MeshRenderer,UnityEngine.BoxCollider]},{name:SketchfabWebRequestManager,components:[UnityEngine.Transform,SketchfabWebRequestManager]}]}
assistant:
Relevant objects: "RightHand".


'''