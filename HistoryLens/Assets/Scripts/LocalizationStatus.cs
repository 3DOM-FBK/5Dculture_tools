/*===============================================================================
Copyright (C) 2024 Immersal - Part of Hexagon. All Rights Reserved.

This file is part of the Immersal SDK.

The Immersal SDK cannot be copied, distributed, or made available to
third-parties for commercial purposes without written permission of Immersal Ltd.

Contact sales@immersal.com for licensing requests.
===============================================================================*/

using System;
using UnityEngine;
using UnityEngine.UIElements;
using TMPro;
using Immersal;
using Immersal.XR;

namespace Immersal.Samples.Util
{

    [RequireComponent(typeof(TextMeshProUGUI))]
    public class LocalizationStatus : MonoBehaviour
    {

        TemplateUI_control templeteUIControl;

        private const string StringFormat = "Successful localizations: {0}/{1}";

        // private TextMeshProUGUI m_LabelText;
        private ImmersalSDK m_Sdk;

        private Label _debug_label;

        void Start()
        {

            templeteUIControl = GameObject.FindGameObjectWithTag("UIDocument").GetComponent<TemplateUI_control>();

            var root = GetComponent<UIDocument>().rootVisualElement;

            _debug_label = root.Q<Label>("debug-label");
            // m_LabelText = GetComponent<TextMeshProUGUI>();
            m_Sdk = ImmersalSDK.Instance;
        }

        void Update()
        {
            if (m_Sdk == null)
                return;

            ITrackingStatus status = m_Sdk.TrackingStatus;
            if (status != null)
            {
                // m_LabelText.text = string.Format(StringFormat, status.LocalizationSuccessCount, status.LocalizationAttemptCount);
                _debug_label.text = string.Format(StringFormat, status.LocalizationSuccessCount, status.LocalizationAttemptCount);
                // Debug.Log(string.Format(StringFormat, status.LocalizationSuccessCount, status.LocalizationAttemptCount));

                if (status.LocalizationSuccessCount > 2)
                {
                    templeteUIControl.HideARIconAnimation();
                }
            }
            
            
        }
    }
}
