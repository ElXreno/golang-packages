%global goipath         github.com/lunny/dingtalk_webhook
%global commit          e3534c89ef969912856dfa39e56b09e58c5f5daf
%global scm             git

%gometa

%global common_description %{expand:
A library encapsulates requests for the webhook portion of Dingtalk.
}

%global golicenses      LICENSE
%global godocs          README.md

Name:                   %{goname}
Version:                0
Release:                1%{?dist}
Summary:                A library encapsulates requests for the webhook portion of Dingtalk.

License:                MIT
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
