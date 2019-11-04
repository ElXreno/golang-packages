%global goipath         github.com/go-macaron/i18n
%global commit          ef57533c3b0fc2d8581deda14937e52f11a203ab
%global scm             git

%gometa

%global common_description %{expand:
Middleware i18n provides app Internationalization and Localization for Macaron
}

%global golicenses      LICENSE
%global godocs          README.md

Name:                   %{goname}
Version:                0
Release:                1%{?dist}
Summary:                Middleware i18n provides app Internationalization and Localization for Macaron

License:                Apache-2.0
URL:                    %{gourl}
Source0:                %{gosource}


%description
%{common_description}

%gopkg


%prep
%goprep


%install
%gopkginstall


%files
%gopkgfiles



%changelog
* Mon Nov  4 2019 ElXreno <elxreno@gmail.com>
- Initial packaging
