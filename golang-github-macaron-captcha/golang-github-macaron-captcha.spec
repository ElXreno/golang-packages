%global goipath         github.com/go-macaron/captcha
%global commit          8dc5911259df0879711118752c6e1a4bb012d410
%global scm             git

%gometa

%global common_description %{expand:
Middleware captcha provides captcha service for Macaron
}

%global golicenses      LICENSE
%global godocs          README.md

Name:                   %{goname}
Version:                0
Release:                1%{?dist}
Summary:                Middleware captcha provides captcha service for Macaron

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
