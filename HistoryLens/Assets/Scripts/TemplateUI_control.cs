using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UIElements;

[Serializable]
public class TemplateUI_control : MonoBehaviour
{

    // VisualElements
    private VisualElement _introductionContainer;
    private VisualElement _mainContainer;
    private VisualElement _debugContainer;
    private VisualElement _animBtnElem;
    private VisualElement _infoContainer;
    private VisualElement _creditContainer;
    private VisualElement _turorialContainer;
    private VisualElement _ARIconContainer;
    private VisualElement _ARIconPhone;

    // Buttons
    private Button _btnCloseIntroduction;
    private Button _btnDebug;
    private Button _btnInfo;
    private Button _btnCredit;
    private Button _btnTutorial;
    private Button _btnCloseInfo;

    private Label _tracking_label;

    // Global Variables
    private bool isDebugOpen = false;

    // Start is called before the first frame update
    void Start()
    {
        var root = GetComponent<UIDocument>().rootVisualElement;

        _introductionContainer = root.Q<VisualElement>("introduction");
        _mainContainer = root.Q<VisualElement>("main");
        _debugContainer = root.Q<VisualElement>("debug");
        _animBtnElem = root.Q<VisualElement>("anim-btn-elem");
        _infoContainer = root.Q<VisualElement>("info");
        _creditContainer = root.Q<VisualElement>("credit-container");
        _turorialContainer = root.Q<VisualElement>("tutorial-container");
        _ARIconContainer = root.Q<VisualElement>("AR-icon-anim");
        _ARIconPhone = root.Q<VisualElement>("Ar-phone");

        _btnCloseIntroduction = root.Q<Button>("btn-close-introduction");
        _btnDebug = root.Q<Button>("btn-debug");
        _btnInfo = root.Q<Button>("btn-info");
        _btnCredit = root.Q<Button>("btn-credit");
        _btnTutorial = root.Q<Button>("btn-tutorial");
        _btnCloseInfo = root.Q<Button>("btn-close-info");

        _btnCloseIntroduction.RegisterCallback<ClickEvent>(OnCloseIntroductionContainer);
        _btnDebug.RegisterCallback<ClickEvent>(OnPressDebugBtn);
        _btnInfo.RegisterCallback<ClickEvent>(OnPressInfoBtn);
        _btnCredit.RegisterCallback<ClickEvent>(OnPressCreditBtn);
        _btnTutorial.RegisterCallback<ClickEvent>(OnPressTutorialBtn);
        _btnCloseInfo.RegisterCallback<ClickEvent>(OnCloseInfoContainer);

        _introductionContainer.style.display = DisplayStyle.Flex;
        _mainContainer.style.display = DisplayStyle.None;
        _infoContainer.style.display = DisplayStyle.None;

        _tracking_label = root.Q<Label>("tracking-label");

        _ARIconPhone.RegisterCallback<TransitionEndEvent>(evt => _ARIconPhone.ToggleInClassList("ar_icon_end"));
        root.schedule.Execute(() => _ARIconPhone.ToggleInClassList("ar_icon_end")).StartingIn(1500);
        ShowARIconAnimation();
    }

    private void OnCloseIntroductionContainer(ClickEvent evt)
    {
        _introductionContainer.AddToClassList("introduction-close");

        StartCoroutine(WaitOpenMainContainer());
    }

    private void OnPressDebugBtn(ClickEvent evt)
    {
        if (isDebugOpen)
        {
            _debugContainer.AddToClassList("debug-hide");
            isDebugOpen = false;
        }
        else {
            _debugContainer.RemoveFromClassList("debug-hide");
            isDebugOpen = true;
        }
    }

    private void OnPressCreditBtn(ClickEvent evt)
    {
        _animBtnElem.RemoveFromClassList("anim_btn_elem_info");
        _btnCredit.RemoveFromClassList("text_disable");
        _btnTutorial.AddToClassList("text_disable");

        ShowCreditContainer();
        HideTutorialContainer();
    }

    private void OnPressTutorialBtn(ClickEvent evt)
    {
        _animBtnElem.AddToClassList("anim_btn_elem_info");
        _btnTutorial.RemoveFromClassList("text_disable");
        _btnCredit.AddToClassList("text_disable");

        ShowTutorialContainer();
        HideCreditContainer();
    }

    private void OnCloseInfoContainer(ClickEvent evt)
    {
        _introductionContainer.style.display = DisplayStyle.None;
        _mainContainer.style.display = DisplayStyle.Flex;
        _infoContainer.style.display = DisplayStyle.None;
    }

    private void OnPressInfoBtn(ClickEvent evt)
    {
        _introductionContainer.style.display = DisplayStyle.None;
        _mainContainer.style.display = DisplayStyle.None;
        _infoContainer.style.display = DisplayStyle.Flex;
    }

    private void HideCreditContainer()
    {
        _creditContainer.style.display = DisplayStyle.None;
    }

    private void ShowCreditContainer()
    {
        _creditContainer.style.display = DisplayStyle.Flex;
    }

    private void HideTutorialContainer()
    {
        _turorialContainer.style.display = DisplayStyle.None;
    }

    private void ShowTutorialContainer()
    {
        _turorialContainer.style.display = DisplayStyle.Flex;
    }

    public void HideARIconAnimation()
    {
        _ARIconContainer.style.display = DisplayStyle.None;
    }

    public void ShowARIconAnimation()
    {
        _ARIconContainer.style.display = DisplayStyle.Flex;
    }

    IEnumerator WaitOpenMainContainer()
    {
        yield return new WaitForSeconds(1);
        _introductionContainer.style.display = DisplayStyle.None;
        _infoContainer.style.display = DisplayStyle.None;
        _mainContainer.style.display = DisplayStyle.Flex;
    }


    public void OnPlatformTrackingLost()
    {
        _tracking_label.text = "Platform Tacking Lost...";
    }

    public void OnTrackingLost()
    {
        _tracking_label.text = "Tacking Lost...";
    }

    public void OnTrackingWell()
    {
        _tracking_label.text = "Tacking Well...";
    }

}
